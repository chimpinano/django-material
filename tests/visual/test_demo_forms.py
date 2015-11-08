# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import VisualTest


class TestLoginForm(VisualTest):
    urls = 'demo.tests.test_forms_login'

    def test_default_usecase(self):
        self.driver.get('%s/demo/login/' % self.live_server_url)
        self.assertScreenshot('.card', 'form_login_default_usecase')

    def test_invalid_data(self):
        self.driver.get('%s/demo/login/' % self.live_server_url)

        self.driver.find_element_by_css_selector("button[type=submit]").click()
        self.assertScreenshot('.card', 'form_login_invalid_data')


class TestRegistrationForm(VisualTest):
    urls = 'demo.tests.test_forms_registration'

    def test_default_usecase(self):
        self.driver.get('%s/demo/registration/' % self.live_server_url)
        self.assertScreenshot('.card', 'form_registration_default_usecase')

    def test_invalid_data(self):
        self.driver.get('%s/demo/registration/' % self.live_server_url)

        self.driver.find_element_by_css_selector("button[type=submit]").click()
        self.assertScreenshot('.card', 'form_registration_invalid_data')


class TestContactForm(VisualTest):
    urls = 'demo.tests.test_forms_contact'

    def test_default_usecase(self):
        self.driver.get('%s/demo/contact/' % self.live_server_url)
        self.assertScreenshot('.card', 'form_contact_default_usecase')

    def test_invalid_data(self):
        self.driver.get('%s/demo/contact/' % self.live_server_url)

        self.driver.find_element_by_css_selector("button[type=submit]").click()
        self.assertScreenshot('.card', 'form_contact_invalid_data')


class TestOrderForm(VisualTest):
    urls = 'demo.tests.test_forms_order'

    def test_default_usecase(self):
        self.driver.get('%s/demo/order/' % self.live_server_url)
        self.assertScreenshot('.card', 'form_order_default_usecase')

    def test_invalid_data(self):
        self.driver.get('%s/demo/order/' % self.live_server_url)

        self.driver.find_element_by_css_selector("button[type=submit]").click()
        self.assertScreenshot('.card', 'form_order_invalid_data')


class TestCheckoutForm(VisualTest):
    urls = 'demo.tests.test_forms_checkout'

    def test_default_usecase(self):
        self.driver.get('%s/demo/checkout/' % self.live_server_url)
        self.assertScreenshot('.card', 'form_checkout_default_usecase')

    def test_invalid_data(self):
        self.driver.get('%s/demo/checkout/' % self.live_server_url)

        self.driver.find_element_by_css_selector("button[type=submit]").click()
        self.assertScreenshot('.card', 'form_checkout_invalid_data')


class TestCommentForm(VisualTest):
    urls = 'demo.tests.test_forms_comment'

    def test_default_usecase(self):
        self.driver.get('%s/demo/comment/' % self.live_server_url)
        self.assertScreenshot('.card', 'form_comment_default_usecase')

    def test_invalid_data(self):
        self.driver.get('%s/demo/comment/' % self.live_server_url)

        self.driver.find_element_by_css_selector("button[type=submit]").click()
        self.assertScreenshot('.card', 'form_comment_invalid_data')


class TestBankForm(VisualTest):
    urls = 'demo.tests.test_forms_bank'

    def test_default_usecase(self):
        self.driver.get('%s/demo/bank/' % self.live_server_url)
        self.assertScreenshot('.card', 'form_bank_default_usecase')

    def test_invalid_data(self):
        self.driver.get('%s/demo/bank/' % self.live_server_url)

        self.driver.find_element_by_css_selector("button[type=submit]").click()
        self.assertScreenshot('.card', 'form_bank_invalid_data')