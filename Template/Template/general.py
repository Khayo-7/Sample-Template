import base64
import imgkit
import datetime
from io import BytesIO 
from xhtml2pdf import pisa
from django.template import Context 
from django.contrib import messages 
from django.views.generic import FormView
from django.http import HttpResponse, Http404
from django.db import IntegrityError, transaction
from django.db.models import Q, CharField, DateField
from django.contrib.postgres.search import SearchVector
from django.template.loader import render_to_string, get_template 
from django.shortcuts import render, redirect, reverse, get_object_or_404


# from cgi import escape
# import cStringIO as StringIO


# Create your views here.
from Template.trans import phrases
from Template.forms import SearchForm

## delete
from users.models import User
from myapp.models import Model1, Model2

# General
class General:  

    def __init__(self, arguments):     

        self.app = arguments['app']
        self.title = arguments['title']
        self.success_url = arguments['success_url'] 
        self.instance = arguments['instance']
        self.instance_type = arguments['instance_type']
        self.form = arguments['form']   
        # self.update_form = arguments['update_form']
        self.serializer = arguments['serializer']  
        self.filter = arguments['filter']  

        self.action = arguments['action'] 
        self.page_type = arguments['page_type']
        self.url_suffix = arguments['url_suffix']
        self.view_all_url = arguments['view_all_url']
        # self.request = arguments['request']
        self.form_template = arguments['form_template']
        self.main_template = arguments['main_template']
        self.view_template = arguments['view_template']
        self.pdf_template = arguments['pdf_template']
        self.view_all_template = arguments['view_all_template']
        self.assurance_template = arguments['assurance_template']

    def get_context(self):
        context = {
                'app': self.app, 
                'title': self.title, 
                'instance_type': self.instance_type, 
                'action': self.action, 
                'page_type': self.page_type, 
                'url_suffix': self.url_suffix, 
                'view_all_url': self.view_all_url
            }
        return context

    def index(self, request):  
        context = self.get_context()
        return render(request, self.main_template, context)
 

    def search(self, request):  

        self.action = "Search"  
        self.page_type = "Result Page"  
        self.form = SearchForm 
        instance = self.instance

        form = self.form(request.POST or request.GET or None)
        context = self.get_context()
        context.update({'form': form})   
         
        if request.method == 'POST' or request.method == 'POST':

            if form.is_valid():
                keyword = form.cleaned_data['keyword'] 

                field_names = [field.name for field in instance._meta.fields if isinstance(field, CharField)]# or isinstance(f, DateField)]
                
                queries = Q()
                for query in [Q(**{field_name + "__icontains": keyword}) for field_name in field_names]:
                    queries = queries | query

                queryset = instance.objects.filter(queries).values()
                # queryset = instance.objects.annotate(search=SearchVector(*field_names),).filter(search__icontains=keyword).values()
                
                filter = self.filter(request.GET, queryset=queryset)
                instances = filter.qs  
                count = instances.count()

                if(instances):
                    context = self.get_context()
                    context.update({'instances': instances, 'count': count, 'filter' : filter})  
                    return render(request, self.view_all_template, context)
                else:
                    messages.add_message(request, messages.INFO, self.instance_type + " not found")
                    return redirect(request.path)    
            else:
                messages.add_message(request, messages.INFO, "Something went wrong. Invalid Search Keywordword")
                return redirect(request.path)    

        return render(request, self.form_template, context)

    def view(self, request, id):

        self.action = "View"
        
        try:
            instance = get_object_or_404(self.instance, pk=id)#, User=self.request.User)
            # instance = instance.objects.get(pk=id)   
            context = self.get_context()
            context.update({'instance': instance, 'full_information': True, 'pagesize':'A4'})  
            type = 'attachment'

            if request.method == 'POST': 
                return self.pdf_generator(request, context, type)

            return render(request, self.view_template, context)
            
        except self.instance.DoesNotExist:
            messages.add_message(request, messages.INFO, self.instance_type + " not found")
            # return redirect(self.success_url)   
            return redirect(request.META.get('HTTP_REFERER')) 
            # return redirect(instance) 
    
    def view_all(self, request):

        self.action = "View All" 
        # instance = self.instance
        print(self.instance)
        try:
            filter = self.filter(request.GET, queryset=self.instance.objects.all())
            instances = filter.qs
            count = instances.count()  
            context = self.get_context()
            context.update({'instances': instances, 'count': count, 'filter' : filter, 'full_information': True, 'pagesize':'A4'})
            type = 'attachment'
            print(count)
            if request.method == 'POST':                 
                return self.pdf_generator(request, context, type)
                    
            return render(request, self.view_all_template, context)
        except instance.DoesNotExist:
            messages.add_message(request, messages.INFO, self.title + " are not found")
            # return redirect(self.success_url)   
            return redirect(request.META.get('HTTP_REFERER')) 
            # return redirect(instance) 

    
    @transaction.atomic 
    def add(self, request):
        
        self.action = "Add"   
        # instance = self.instance
        context = self.get_context()
        
        form = self.form(request.POST or None, request.FILES or None)     
        context.update({'form': form}) 

        if request.method == 'POST':

            if form.is_valid():
                try:
                    with transaction.atomic():  

                        add_form = form.save(commit=False)

                        try:
                            usr = User.objects.get(pk=1)
                            add_form.created_by = usr # form.created_by = request.User

                        except:                        
                            add_form.created_by =None
                        add_form.updated_by = None
                        add_form.updated_at = None
                        add_form.save()

                            
                        # messages.DEBUG INFO SUCCESS WARNING ERROR
                        messages.add_message(request, messages.INFO, self.instance_type + " is Created Successfully")

                        if request.POST['submit'] == 'add':
                            return redirect(request.path) 
                        return redirect(self.success_url)
                        
                except IntegrityError:
                            messages.add_message(request, messages.INFO, self.instance_type + " cannot be created. Issue with Integrity")
                            return redirect(request.path) 
            else:
                messages.add_message(request, messages.INFO, self.instance_type + " cannot be created. Invalid Form")
                return redirect(request.path)   
        return render(request, self.form_template, context)
    
    @transaction.atomic       
    def update(self, request, id):        
        
        self.action = "Update"  
        # instance = self.instance
        context = self.get_context()

        instance = self.instance.objects.get(pk=id)
        form = self.form(request.POST or None, instance=instance)             
        context.update({'form': form})

        if request.method == 'POST':
            if form.is_valid():
                try:
                    with transaction.atomic():                 
                        form = form.save(commit=False)
                        usr = User.objects.get(pk=1)
                        form.updated_by = usr                
                        # form.updated_by = request.User
                        form.save()
                        messages.add_message(request, messages.INFO, self.instance_type + " is Updated Successfully")
                        return redirect(self.success_url)

                except IntegrityError:
                    messages.add_message(request, messages.INFO, self.instance_type + " cannot be created. Issue with Integrity")
                    return redirect(request.path)
            else:
                messages.add_message(request, messages.INFO, self.instance_type + " cannot be updated. Invalid Form")
                return redirect(request.path)   
        
        return render(request, self.form_template, context)    

    @transaction.atomic 
    def delete(self, request, id):
        
        self.action = "Delete"
        # instance = self.instance
        context = self.get_context()

        instance = self.instance.objects.get(pk=id)
        context.update({'instance': instance})

        if request.method == 'POST':     
            try:
                with transaction.atomic(): 

                    instance.delete()
                    messages.add_message(request, messages.INFO, self.instance_type + " is Deleted Successfully") 
                    return redirect(self.success_url)  

            except IntegrityError:
                messages.add_message(request, messages.INFO, self.instance_type + " cannot be deleted. Issue with Integrity")
                return redirect(request.path) 
        
        return render(request, self.assurance_template, context)
        
    def approve(self, request, id):

        self.action = "Approve"
        status = 'approved'
        return self.approve_reject(request, id, self.action, status)
        
    def reject(self, request, id):
        
        self.action = "Reject"
        status = 'rejected'
        return self.approve_reject(request, id, self.action, status)
    
    @transaction.atomic
    def approve_reject(self, request, id, action, status):        
        
        self.action = action
        # instance = self.instance
        context = self.get_context()

        instance = self.instance.objects.get(pk=id)
        context.update({'instance': instance})

        if request.method == 'POST':
            
            if instance.status == 'pending':
                try:
                    with transaction.atomic():  

                        instance.approved_by = None
                        instance.status = status
                        instance.save()
                        
                        messages.add_message(request, messages.INFO, self.instance_type + " is " + status)
                        return redirect(self.success_url)
            
                except IntegrityError:
                    messages.add_message(request, messages.INFO, self.instance_type + " cannot be " + status + ". Issue with Integrity")
                    return redirect(request.path) 
            else:
                messages.add_message(request, messages.INFO, self.instance_type + " cannot be " + status)
                return redirect(request.path)   
        
        return render(request, self.assurance_template, context)
         
    def pdf_generator(self, request, context, type):

        if request.POST['submit'] == 'preview-partial':
            type = 'inline'
            context['full_information'] = False
            
        elif request.POST['submit'] == 'preview-full':
            type = 'inline'
            
        elif request.POST['submit'] == 'download-partial':
            context['full_information'] = False

        return self.generate_pdf(request, context, type)

    def pdf_generator_2(self, request, id, preference, state):
        
        instance = self.instance 
        context = self.get_context()

        instance = get_object_or_404(instance, pk=id)#, User=request.User)
        context.update({'pagesize':'A4', 'full_information': False, 'instance': instance})
        type='attachment'

        if preference == 'preview':
            type = 'inline'
        if state == 'full':
            context['full_information'] = True

        return self.generate_pdf(request, context, type)
 
    def generate_pdf(self, request, context, type):   


        # from cgi import escape
        from reportlab.pdfgen import canvas
        from reportlab.lib.utils import ImageReader
        
        
        result = BytesIO()
        # # result = StringIO.StringIO()
        # now = str(datetime.datetime.utcnow().strftime('%H:%M:%S %d-%m-%Y')) 
        # now = str(datetime.datetime.now())[:-7]
        # now = ('_').join(now.split())

        now = str(datetime.datetime.now().strftime('%d-%m-%Y_%Hhr:%Mmin:%Ssec'))

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = type + '; filename=report_%s.pdf' % now
        response['Content-Encoding'] = 'UTF-8'
        template = get_template(self.pdf_template)
        # context = Context(context)
        html  = template.render(context)
        
        pisa_pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)        
        if pisa_pdf.err:
            return HttpResponse('Error <pre>' + html + '</pre>' % escape(html))

        # cnvs = canvas.Canvas(result)

        # header_image = ImageReader('/home/khalid/Template/Template/static/img/header.png')
        # footer_image = ImageReader('/home/khalid/Template/Template/static/img/footer.png')
        # cnvs.drawImage(header_image, -100, 700, mask='auto')
        # cnvs.drawImage(footer_image, -100, 100, mask='auto')
        # cnvs.drawString(300, 830, "Report Created At " + now )
        # cnvs.showPage() 
        # cnvs.save() 
            
        
        response.write(result.getvalue())
        result.close()
        return response



     

    # def download_docx(self, request, pdf_template, context, type='attachment'):


        from django.http import FileResponse
        from docxtpl import DocxTemplate

        from docx import Document
        # from django.http import HttpResponse

        result = BytesIO()
        # # result = StringIO.StringIO()

        now = str(datetime.datetime.now().strftime('%d-%m-%Y_%Hhr:%Mmin:%Ssec'))

        response = HttpResponse(content_type='application/pdf')
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = type + '; filename=report_%s.docx' % now
        response['Content-Encoding'] = 'UTF-8'

        template = get_template(self.pdf_template)
        # context = Context(context)
        html  = template.render(context)
        html = render_to_string(self.pdf_template, context)

        # result = BytesIO(html.encode("ISO-8859-1"))
        
        document = Document()
        # document.add_heading('Document Title', 0)
        # document.add_paragraph('Intense quote', style='IntenseQuote') 
        # document.add_paragraph(
        #             'first item in unordered list', style='ListBullet'
        #             )
        # document.add_paragraph(
        #             'first item in ordered list', style='ListNumber'
        #             )

        # #document.add_picture('monty-truth.png', width=Inches(1.25))

        # table = document.add_table(rows=1, cols=3)
        # hdr_cells = table.rows[0].cells
        # hdr_cells[0].text = 'Qty'
        # hdr_cells[1].text = 'Id'
        # hdr_cells[2].text = 'Desc'

        # document.add_page_break()
        # Report = ReportWord(Gcas, FI, FF, grafica)
        # Report.save(result)  # save to memory stream
        # result.seek(0)  # rewind the stream
        
        # context = {'first_name' : 'xxx', 'sur_name': 'yyy'}
        # tpl = DocxTemplate(html)
        # tpl = DocxTemplate(os.path.join(BASE_PATH, 'template.docx'))
        # tpl.render(context)
        # tpl.save(result)
        # return FileResponse(result, as_attachment=True, filename='report_%s.docx' % ('_').join(str(datetime.datetime.now()).split()))

       
        # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        result.seek(0)
        response.write(result.getvalue())
        result.close()
        document.save(response)

        return response      


# weasyprint.HTML(string=html).write_pdf(response,
#     stylesheets=[weasyprint.CSS(
#         settings.STATIC_ROOT + 'css/pdf.css')])


     


    def html_to_image(self, request, pdf_template, context):

        template = get_template(pdf_template)
        # context = Context(context)
        html  = template.render(context)

        response = imgkit.from_file(html, 'report_%s.jpg' % ('_').join(str(datetime.datetime.now()).split()))    
        return response
        # from html2image import Html2Image
        # hti = Html2Image()
        # hti.screenshot(url='https://www.python.org', save_as='python_org.png')
        # orwith open('./test.html') as f:
        #     hti.screenshot(f.read(), save_as='out.png')
        # # pip install htmlwebshot

        # from htmlwebshot import WebShot
        # shot = WebShot()
        # shot.quality = 100

        # image = shot.create_pic(html="file.html")








        # from reportlab.pdfgen import canvas
        # from reportlab.lib.utils import ImageReader
        
        # response = HttpResponse(html, content_type='application/pdf') 

        # response['Content-Disposition'] = type + '; filename=report_%s.pdf' % ('_').join(str(datetime.datetime.now()).split())
          
        # # get_param = request.GET.get('name', 'World')

        # now = datetime.datetime.utcnow().strftime(' %H:%M:%S %d-%m-%Y') #.%f

        # result = BytesIO()
        # p = canvas.Canvas(result)

        # # my_image = ImageReader('https://www.google.com/images/srpr/logo11w.png')

        # # p.drawImage(my_image, 10, 10, mask='auto')

        # p.drawString(10, 830, "Report Created At " + now ) 

        # p.showPage() 
        # p.save() 

        # pdf = result.getvalue()
        # result.close()
        # response.write(pdf)

        # return response

        # doc = SimpleDocTemplate("/tmp/somefilename.pdf")
        # styles = getSampleStyleSheet()
        # Story = [Spacer(1,2*inch)]
        # style = styles["Normal"]
        # for i in range(100):
        #    bogustext = ("This is Paragraph number %s.  " % i) * 20
        #    p = Paragraph(bogustext, style)
        #    Story.append(p)
        #    Story.append(Spacer(1,0.2*inch))
        # doc.build(Story)

        # fs = FileSystemStorage("/tmp")
        # with fs.open("somefilename.pdf") as pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        #     return response

        # return response

        # from django.core.files.storage import FileSystemStorage
        # from django.http import HttpResponse
        # from django.template.loader import render_to_string

        # from weasyprint import HTML

    
        # html_string = render_to_string(template_path, context)

        # html = HTML(string=html_string)
        
        # with fs.open('mypdf.pdf') as pdf:
        #     response = HttpResponse(html.write_pdf(), content_type='application/pdf')
        #     response['Content-Disposition'] = 'inline; filename=report_%s.pdf' % ('_').join(str(datetime.datetime.now()).split())
        #     return response

        # return response

        # html.write_pdf(target='/tmp/mypdf.pdf')
        # fs = FileSystemStorage('/tmp')
        # with fs.open('mypdf.pdf') as pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     response['Content-Disposition'] = 'inline; filename=report_%s.pdf' % ('_').join(str(datetime.datetime.now()).split())
        #     return response