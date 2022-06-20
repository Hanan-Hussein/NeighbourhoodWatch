from hashlib import new
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Neighbourhood,Businesses,Posts

# Create your tests here.

class UserTestClass(TestCase):
    def setUp(self):
        self.new_user=User(
            username='jaffar',email='jaff@gmail.com',password='pass1'
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save_method(self):
        self.new_user.save()
        user=User.objects.all()
        self.assertEquals(len(user),1)
    
    def test_delete_method(self):
        self.new_user.save()
        self.new_user.delete()
        user = User.objects.all()
        self.assertFalse(User.objects.filter(pk=self.new_user.id).exists())

class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.new_user=User(
            username='jaffar',email='jaff@gmail.com',password='pass1'
        )
        self.new_user.save()
        self.neighbourhood = Neighbourhood(
            name="Akiba",location="South c",police="+254718056434",health="+254711222222",
            handyman="+254766666789",admin=self.new_user
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))
        def test_save_profile(self):
            self.neighbourhood.save()
            images = Neighbourhood.objects.all()

            self.assertEquals(len(images),1)

    def test_delete_image(self):
        def setUp(self):
            self.user=User(
                username='jaffar',email='jaff@gmail.com',password='pass1')
            self.user.save()
            self.neighbourhood = Neighbourhood(
                    name="Akiba",location="South c",police="+254718056434",health="+254711222222",
                    handyman="+254766666789",admin=self.new_user
                )            
            self.neighbourhood.delete()
            neighbourhood = Neighbourhood.objects.all()

        self.assertFalse(Neighbourhood.objects.filter(pk=self.neighbourhood.id).exists())
    
    def test_find_neighbourhood(self):
         def setUp(self):
            self.user=User(
                username='jaffar',email='jaff@gmail.com',password='pass1')
            self.user.save()
            self.neighbourhood = Neighbourhood(
                    name="Akiba",location="South c",police="+254718056434",health="+254711222222",
                    handyman="+254766666789",admin=self.new_user
                )    
            self.neighbourhood.find_neigborhood(self.neighbourhood.id)

class ProfileTestClass(TestCase):
  
    def setUp(self):
        self.user=User(
            username='bb',email='bb@gmail.com',password='pass1'
    )
        self.neighbourhood = Neighbourhood(
            name="Akiba",location="South c",police="+254718056434",health="+254711222222",
            handyman="+254766666789",admin=self.user
        )
        self.profile=Profile(user=self.user,neighbourhood=self.neighbourhood)

        self.user.save()
        self.neighbourhood.save()

 
    def test_save_profile(self):
        profiles = Profile.objects.all()

        self.assertEquals(len(profiles),1)

class BusinessesTestCase(TestCase):
    def setUp(self):
        self.new_user=User(
            username='jaffar',email='jaff@gmail.com',password='pass1'
        )
        self.neighbourhood = Neighbourhood(
            name="Akiba",location="South c",police="+254718056434",health="+254711222222",
            handyman="+254766666789",admin=self.new_user
        )
        self.new_user.save()
        self.neighbourhood.save()
        
        self.business=Businesses(
            name="Hanan's Coffee",user=self.new_user,neighbourhood=self.neighbourhood,
            email="hanhuss035@gmail.com",description="Hanan's Coffee is delicious",business_image="https://picsum.photos/200/300"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))
        def test_save_business(self):
            self.business.save()
            bs = Businesses.objects.all()

            self.assertEquals(len(bs),1)

    def test_delete_business(self):
        def setUp(self):
            self.new_user=User(
                username='jaffar',email='jaff@gmail.com',password='pass1'
            )
            self.neighbourhood = Neighbourhood(
                name="Akiba",location="South c",police="+254718056434",health="+254711222222",
                handyman="+254766666789",admin=self.new_user
            )
            self.new_user.save()
            self.neighbourhood.save()
            
            self.business=Businesses(
                name="Hanan's Coffee",user=self.new_user,neighbourhood=self.neighbourhood,
                email="hanhuss035@gmail.com",description="Hanan's Coffee is delicious",business_image="https://picsum.photos/200/300"
            )
        self.assertFalse(Businesses.objects.filter(pk=self.business.id).exists())
    
    def test_find_businesses(self):
        def setUp(self):
            self.new_user=User(
                username='jaffar',email='jaff@gmail.com',password='pass1'
            )
            self.neighbourhood = Neighbourhood(
                name="Akiba",location="South c",police="+254718056434",health="+254711222222",
                handyman="+254766666789",admin=self.new_user
            )
            self.new_user.save()
            self.neighbourhood.save()
            
            self.business=Businesses(
                name="Hanan's Coffee",user=self.new_user,neighbourhood=self.neighbourhood,
                email="hanhuss035@gmail.com",description="Hanan's Coffee is delicious",business_image="https://picsum.photos/200/300"
            )
            self.business.find_businesses(self.business.id)
