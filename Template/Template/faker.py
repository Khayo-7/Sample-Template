import random
from faker import Faker

fake = Faker()
# fake = Faker(['it_IT', 'en_US', 'ja_JP', 'hi_IN'])

def generate_random_data(model, n=10)->bool:
    [model.objects.create(
        code = fake.name(),
        name = fake.name(),
        description = fake.text(),
        # profile = fake.profile(),
        # address = fake.address(),
        # email = fake.email(),
        # country = fake.country(),
        # (fake.latitude(), fake.longitude()),
        #  with open('students.json', 'w') as fp: 
        #       json.dump(student_data, fp) 

    ) for i in range(n)]

    return True


# names = [fake.unique.first_name() for i in range(500)]
# assert len(set(names)) == len(names)


# for i in range(3):
#      # Raises a UniquenessException
#      fake.unique.boolean()

# fake.unique.clear() 


# # first, import a similar Provider or use the default one
# from faker.providers import BaseProvider

# # create new provider class
# class MyProvider(BaseProvider):
#     def foo(self) -> str:
#         return 'bar'

# # then add new provider to faker instance
# fake.add_provider(MyProvider)

# # now you can use:
# fake.foo()
# # 'bar'


# from faker.providers import DynamicProvider

# medical_professions_provider = DynamicProvider(
#      provider_name="medical_profession",
#      elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
# )

# # then add new provider to faker instance
# fake.add_provider(medical_professions_provider)

# # now you can use:
# fake.medical_profession()
# # 'dr.'

# my_word_list = [
# 'danish','cheesecake','sugar',
# 'Lollipop','wafer','Gummies',
# 'sesame','Jelly','beans',
# 'pie','bar','Ice','oat' ]

# fake.sentence()
# # 'Expedita at beatae voluptatibus nulla omnis.'

# fake.sentence(ext_word_list=my_word_list)
# # 'Oat beans oat Lollipop bar cheesecake.'


# from model_utils.fields import MonitorField, StatusField

# class Article(models.Model):
#     STATUS = Choices('draft', 'published')

#     status = StatusField()
#     published_at = MonitorField(monitor='status', when=['published'])

# from django.db import models
# from model_utils.fields import UUIDField

# class MyAppModel(models.Model):
#     uuid = UUIDField(primary_key=True, version=4, editable=False)

# import uuid

# from django.db import models
# from model_utils.fields import UrlsafeTokenField


# def _token_factory(max_length):
#     return uuid.uuid4().hex


# class MyAppModel(models.Model):
#     uuid = UrlsafeTokenField(max_length=32, factory=_token_factory)
