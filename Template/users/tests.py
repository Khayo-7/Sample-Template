# from django.test import TestCase

# # Create your tests here.
# forms.py

# from django import forms

# class LinkForm(forms.Form):
#     """
#     Form for individual user links
#     """
#     anchor = forms.CharField(
#                     max_length=100,
#                     widget=forms.TextInput(attrs={
#                         'placeholder': 'Link Name / Anchor Text',
#                     }),
#                     required=False)
#     url = forms.URLField(
#                     widget=forms.URLInput(attrs={
#                         'placeholder': 'URL',
#                     }),
#                     required=False)

#         forms.py

# class ProfileForm(forms.Form):
#     """
#     Form for user to update their own profile details
#     (excluding links which are handled by a separate formset)
#     """
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super(ProfileForm, self).__init__(*args, **kwargs)

#         self.fields['first_name'] = forms.CharField(
#                                         max_length=30,
#                                         initial = self.user.first_name,
#                                         widget=forms.TextInput(attrs={
#                                             'placeholder': 'First Name',
#                                         }))
#         self.fields['last_name'] = forms.CharField(
#                                         max_length=30,
#                                         initial = self.user.last_name,
#                                         widget=forms.TextInput(attrs={
#                                             'placeholder': 'Last Name',
#                                         }))

#                                         forms.py

# from django.forms.formsets import BaseFormSet

# class BaseLinkFormSet(BaseFormSet):
#     def clean(self):
#         """
#         Adds validation to check that no two links have the same anchor or URL
#         and that all links have both an anchor and URL.
#         """
#         if any(self.errors):
#             return

#         anchors = []
#         urls = []
#         duplicates = False

#         for form in self.forms:
#             if form.cleaned_data:
#                 anchor = form.cleaned_data['anchor']
#                 url = form.cleaned_data['url']

#                 # Check that no two links have the same anchor or URL
#                 if anchor and url:
#                     if anchor in anchors:
#                         duplicates = True
#                     anchors.append(anchor)

#                     if url in urls:
#                         duplicates = True
#                     urls.append(url)

#                 if duplicates:
#                     raise forms.ValidationError(
#                         'Links must have unique anchors and URLs.',
#                         code='duplicate_links'
#                     )

#                 # Check that all links have both an anchor and URL
#                 if url and not anchor:
#                     raise forms.ValidationError(
#                         'All links must have an anchor.',
#                         code='missing_anchor'
#                     )
#                 elif anchor and not url:
#                     raise forms.ValidationError(
#                         'All links must have a URL.',
#                         code='missing_URL'
#                     )


#                     views.py

# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
# from django.db import IntegrityError, transaction
# from django.forms.formsets import formset_factory
# from django.shortcuts import redirect, render
# from myapp.forms import LinkForm, BaseLinkFormSet, ProfileForm
# from myapp.models import UserLink

# @login_required
# def test_profile_settings(request):
#     """
#     Allows a user to update their own profile.
#     """
#     user = request.user

#     # Create the formset, specifying the form and formset we want to use.
#     LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

#     # Get our existing link data for this user.  This is used as initial data.
#     user_links = UserLink.objects.filter(user=user).order_by('anchor')
#     link_data = [{'anchor': l.anchor, 'url': l.url}
#                     for l in user_links]

#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, user=user)
#         link_formset = LinkFormSet(request.POST)

#         if profile_form.is_valid() and link_formset.is_valid():
#             # Save user info
#             user.first_name = profile_form.cleaned_data.get('first_name')
#             user.last_name = profile_form.cleaned_data.get('last_name')
#             user.save()

#             # Now save the data for each form in the formset
#             new_links = []

#             for link_form in link_formset:
#                 anchor = link_form.cleaned_data.get('anchor')
#                 url = link_form.cleaned_data.get('url')

#                 if anchor and url:
#                     new_links.append(UserLink(user=user, anchor=anchor, url=url))

#             try:
#                 with transaction.atomic():
#                     #Replace the old with the new
#                     UserLink.objects.filter(user=user).delete()
#                     UserLink.objects.bulk_create(new_links)

#                     # And notify our users that it worked
#                     messages.success(request, 'You have updated your profile.')

#             except IntegrityError: #If the transaction failed
#                 messages.error(request, 'There was an error saving your profile.')
#                 return redirect(reverse('profile-settings'))

#     else:
#         profile_form = ProfileForm(user=user)
#         link_formset = LinkFormSet(initial=link_data)

#     context = {
#         'profile_form': profile_form,
#         'link_formset': link_formset,
#     }

#     return render(request, 'our_template.html', context)


#     edit_profile.html

# {% load staticfiles %}

# {% if messages %}
#     {% for message in messages %}
#         <p>{{ message }}</p>
#     {% endfor %}
# {% endif %}

# <form method="post">
#     {% csrf_token %}

#     <label>First Name</label>
#     {{ profile_form.first_name }}
#     {% if profile_form.first_name.errors %}
#         {% for error in profile_form.first_name.errors %}
#             {{ error|escape }}
#         {% endfor %}
#     {% endif %}

#     <label>Last Name</label>
#     {{ profile_form.last_name }}
#     {% if profile_form.last_name.errors %}
#         {% for error in profile_form.last_name.errors %}
#             {{ error|escape }}
#         {% endfor %}
#     {% endif %}

#     {{ link_formset.management_form }}

#     {% for link_form in link_formset %}
#         <div class="link-formset">
#             {{ link_form.anchor }}
#             {% if link_form.anchor.errors %}
#                 {% for error in link_form.anchor.errors %}
#                     {{ error|escape }}
#                 {% endfor %}
#             {% endif %}

#             {{ link_form.url }}
#             {% if link_form.url.errors %}
#                 {% for error in link_form.url.errors %}
#                     {{ error|escape }}
#                 {% endfor %}
#             {% endif %}
#         </div>
#     {% endfor %}

#     {% if link_formset.non_form_errors %}
#         {% for error in link_formset.non_form_errors %}
#             {{ error|escape }}
#         {% endfor %}
#     {% endif %}

#     <input type="submit" value="Update Profile" class="button"/>
# </form>

# <!-- Include formset plugin - including jQuery dependency -->
# <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
# <script src="{% static 'path_to/jquery.formset.js' %}"></script>
# <script>
#     $('.link-formset').formset({
#         addText: 'add link',
#         deleteText: 'remove'
#     });
# </script>



# tests/test_forms.py

# from django.test import TestCase
# from myapp.factories import UserFactory
# from myapp.forms import ProfileForm

# class ProfileFormTest(TestCase):
#     def setUp(self):
#         self.user = UserFactory()
#         self.client.login(username=self.user.email, password='pass')

#     def form_data(self, first, last):
#         return ProfileForm(
#             user=self.user,
#             data={
#                 'first_name': first,
#                 'last_name': last,
#             }
#         )

#     def test_valid_data(self):
#         form = self.form_data('First', 'Last')
#         self.assertTrue(form.is_valid())

#     def test_missing_first_name(self):
#         form = self.form_data('', 'Last')
#         errors = form['first_name'].errors.as_data()
#         self.assertEqual(len(errors), 1)
#         self.assertEqual(errors[0].code, 'required')

#     def test_missing_last_name(self):
#         form = self.form_data('First', '')
#         errors = form['last_name'].errors.as_data()

#         self.assertEqual(len(errors), 1)
#         self.assertEqual(errors[0].code, 'required')



# tests/test_forms.py

# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from myapp.factories import UserFactory
# from myapp.forms import ProfileForm

# class LinkFormsetTest(TestCase):
#     def setUp(self):
#         self.user = UserFactory()
#         self.client.login(username=self.user.email, password='pass')

#     def form_data(self, anchor, url):
#         return ProfileForm(
#             user=self.user,
#             data={
#                 'first_name': 'First',
#                 'last_name': 'Last',
#                 'form-TOTAL_FORMS': 1,
#                 'form-INITIAL_FORMS': 0,
#                 'form-0-anchor': anchor,
#                 'form-0-url': url,
#             }
#         )

#     def post_data(self, anchor1, url1, anchor2='', url2=''):
#         return self.client.post(
#             reverse('test:profile-settings'),
#             data={
#                 'form-TOTAL_FORMS': 2,
#                 'form-INITIAL_FORMS': 0,
#                 'form-0-anchor': anchor1,
#                 'form-0-url': url1,
#                 'form-1-anchor': anchor2,
#                 'form-1-url': url2,
#             }
#         )

#     def raise_formset_error(self, response,error):
#         self.assertFormsetError(
#             response,
#             formset='link_formset',
#             form_index=None,
#             field=None,
#             errors=error
#         )

#     def test_valid_data(self):
#         form = self.form_data('My Link', 'http://mylink.com')
#         self.assertTrue(form.is_valid())

#     def test_empty_fields(self):
#         """
#         Test validation passes when no data is provided
#         (data is not required).
#         """
#         form = self.form_data('', '')
#         self.assertTrue(form.is_valid())

#     def test_duplicate_anchors(self):
#         """
#         Test validation fails when an anchor is submitted more than once.
#         """
#         response = self.post_data('My Link', 'http://mylink.com',
#                                   'My Link', 'http://mylink2.com')

#         self.raise_formset_error(response,
#                                  'Links must have unique anchors and URLs.')

#     def test_duplicate_url(self):
#         """
#         Test validation fails when a URL is submitted more than once.
#         """
#         response = self.post_data('My Link', 'http://mylink.com',
#                                   'My Link2', 'http://mylink.com')

#         self.raise_formset_error(response,
#                                  'Links must have unique anchors and URLs.')

#     def test_anchor_without_url(self):
#         """
#         Test validation fails when a link is submitted without a URL.
#         """
#         response = self.post_data('My Link', '')

#         self.raise_formset_error(response, 'All links must have a URL.')

#     def test_url_without_anchor(self):
#         """
#         Test validation fails when a link is submitted without an anchor.
#         """
#         response = self.post_data('', 'http://mylink.com')

#         self.raise_formset_error(response, 'All links must have an anchor.')



#         tests/test_views.py

# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from myapp.factories import UserFactory
# from myapp.models import User, UserLink

# class ProfileSettingsTest(TestCase):
#     def test_can_update_profile(self):
#         user = UserFactory()
#         self.client.login(username=user.email, password='pass')
#         response = self.client.post(
#             reverse('test:profile-settings'),
#             data={
#                 'first_name': 'New First Name',
#                 'last_name': 'New Last Name',
#                 'form-TOTAL_FORMS': 1,
#                 'form-INITIAL_FORMS': 0,
#                 'form-0-anchor': 'My Link',
#                 'form-0-url': 'http://mylink.com',
#             },
#         )

#         # Get the user again
#         user = User.objects.get(id=user.id)
#         user_link = UserLink.objects.get(user=user)

#         self.assertEqual(user.first_name, 'New First Name')
#         self.assertEqual(user.last_name, 'New Last Name')
#         self.assertEqual(user_link.anchor, 'My Link')
#         self.assertEqual(user_link.url, 'http://mylink.com/')