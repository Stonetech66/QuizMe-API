from django.test import TestCase
from Users.models import User
from .models import Question
# Create your tests here.
from rest_framework.test import RequestsClient, APIClient, APITestCase

class Quiztest(APITestCase):

    def  setUp(self):
        self.user= User.objects.create_user(username="pete", email="p@gmail.com", password="qwerru")
        self.user2= User.objects.create_user(username="peter", email="pe@gmail.com", password="qwerru")
        self.question=Question.objects.create(question="how", user=self.user)
        self.client=APIClient()
        self.url="http://127.0.0.1:8000/"

    def test_list_questions_of_user(self):
        response=self.client.get(f"{self.url}{self.user.id}/")
        no_response=self.client.get(f"{self.url}/8340343/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)


    def test_authenticated_user_can_create_question(self):
        self.client.force_authenticate(user=self.user)
        p=self.client.post(f"{self.url}", data={"question":"po", "user":self.user.id}, format="json")
        self.assertEqual(p.status_code, 201)


    def test_unauthenticated_user_cant_create_question(self):
        p=self.client.post(f"{self.url}", data={"question":"po", "user":self.user.id}, format="json")
        self.assertEqual(p.status_code, 401)

    def test_unauthenticated_users_cant_answer_questions(self):
        p=self.client.post(f"{self.url}answer-question/", data={"question":self.question.id, "answer":"poor", "user":self.user.id})
        self.assertEqual(p.status_code, 401)

    def test_authenticated_users_can_answer_questions(self):
        self.client.force_authenticate(user=self.user)
        p=self.client.post(f"{self.url}answer-question/", data={"question":self.question.id, "answer":"poor", "user":self.user.id})
        self.assertEqual(p.status_code, 201)


    def test_all_users_can_access_schema_docs(self):
        p=self.client.get(f"{self.url}docs/")
        self.assertEqual(p.status_code, 200)

    def test_only_authenticated_user_and_owner_can_update_question(self):
        self.client.force_authenticate(user=self.user)
        p=self.client.put(f"{self.url}1/", data={"question":"po"})
        self.assertEqual(p.status_code, 200)

    def test_authenticated_user_and_not_owner_cant_update_question(self):
        self.client.force_authenticate(user=self.user2)
        p=self.client.put(f"{self.url}1/", data={"question":"po"})
        self.assertEqual(p.status_code, 403)

    def test_unauthenticated_user_cant_update_question(self):
        p=self.client.put(f"{self.url}1/", data={"question":"po"})
        self.assertEqual(p.status_code, 401)


    def test_only_authenticated_user_and_owner_can_delete_question(self):
        self.client.force_authenticate(user=self.user)
        p=self.client.delete(f"{self.url}1/")
        self.assertEqual(p.status_code, 204)

    def test_authenticated_user_and_not_owner_cant_delete_question(self):
        self.client.force_authenticate(user=self.user2)
        p=self.client.delete(f"{self.url}1/")
        self.assertEqual(p.status_code, 403)

    def test_unauthenticated_user_cant_delete_question(self):
        p=self.client.delete(f"{self.url}1/")
        self.assertEqual(p.status_code, 401)

    def test_authenticated_user_can_see_all_users_that_have_answered_his_question(self):
        self.client.force_authenticate(user=self.user)
        p=self.client.get(f"{self.url}all/")
        self.assertEqual(p.status_code, 200)

    def test_unauthenticated_user_cannot_see_all_users_that_have_answered_his_question(self):
        p=self.client.get(f"{self.url}all/")
        self.assertEqual(p.status_code, 401)

    def test_authenticated_user_can_see_every_question_he_has_answered(self):
        self.client.force_authenticate(user=self.user)
        p=self.client.get(f"{self.url}my-answers/")
        self.assertEqual(p.status_code, 200)

    def test_unauthenticated_user_cannot_see_every_question_he_has_answered(self):
        p=self.client.get(f"{self.url}my-answers/")
        self.assertEqual(p.status_code, 401)        

    def test_authenticated_user_can_see_detail_of_a_user_question_who_answerd_his_question(self):
        self.client.force_authenticate(user=self.user)
        p=self.client.get(f"{self.url}answers/{self.user.id}/")
        self.assertEqual(p.status_code, 200)

    def test_unauthenticated_user_cannot_see_detail_of_a_user_question_who_answerd_his_question(self):
        p=self.client.get(f"{self.url}answers/{self.user.id}/")
        self.assertEqual(p.status_code, 401)
