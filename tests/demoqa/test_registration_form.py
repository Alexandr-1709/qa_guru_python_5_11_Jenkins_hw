
import allure
from selene import have, command


@allure.title('Successful fill form')
def test_practice_form(setup_browser):
    browser = setup_browser
    with allure.step('Open registrations form'):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    # WHEN
    with allure.step('fill registration form'):
        browser.element('#firstName').type('Aleksandr')

        browser.element('#lastName').type('Nikiforov')

        browser.element('#userEmail').type('nikiforov@mail.ru')

        # browser.element('[name=gender][value=Male]').double_click()
        browser.all('[name=gender]').element_by(have.value('Male')).double_click()

        browser.element('#userNumber').type('9009997733')

        browser.element('#dateOfBirthInput').press()

        browser.element('.react-datepicker__month-select').send_keys('September')
        browser.element('.react-datepicker__year-select').send_keys('1982')
        browser.element(f'.react-datepicker__day--0{17}').click()

        browser.element('#subjectsInput').type("Computer Science").press_enter()

        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Sports')).click()
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Music')).click()

        # browser.element('#uploadPicture').send_keys(os.getcwd() + "/test_5_5.jpg")
        # browser.element('#uploadPicture').send_keys(os.path.abspath(
        #   os.path.join(os.path.dirname(__file__), os.path.pardir, 'resourсes/test_5_5.jpg')))

        browser.element('#currentAddress').type('Moscow, Vernadsky avenue,19')

        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
        browser.element('#react-select-4-input').type('Delhi').press_enter()

        browser.element('#submit').press_enter()

    # THEN
    with allure.step('Check form results'):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        # browser.element('.table').all('td').even.should(have.texts
        #                                                 ('Aleksandr Nikiforov',
        #                                                  'nikiforov@mail.ru',
        #                                                  'Male',
        #                                                  '9009997733',
        #                                                  '17 September,1982',
        #                                                  'Computer Science',
        #                                                  'Sports, Music',
        #                                                  '',
        #                                                  'Moscow, Vernadsky avenue,19',
        #                                                  'NCR Delhi'))

    # browser.element('#closeLargeModal').press_enter()


