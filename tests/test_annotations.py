import allure
from selene import browser, have


@allure.title("Проверка отображения названия Issue в GitHub")
@allure.tag("UI", "GitHub", "Issue")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("GitHub Issues")
@allure.story("Просмотр информации об Issue")
@allure.link("https://github.com/dascha067-prog/QA_GURU_BELEVTSEVA_HW_5")
@allure.testcase("TESTCASE-007", "Тест-кейс проверки заголовка Issue")
def test_issue_title_is_visible():
    repo = "dascha067-prog/QA_GURU_BELEVTSEVA_HW_5"
    expected_title = "Test issue B"

    open_issues_page(repo)
    open_issue_by_title(expected_title)
    should_have_issue_title(expected_title)


@allure.step("Открыть страницу Issues репозитория: {repo}")
def open_issues_page(repo):
    browser.open(f"https://github.com/{repo}/issues")


@allure.step("Открыть Issue по заголовку: {title}")
def open_issue_by_title(title):
    browser.all('[data-testid="issue-pr-title-link"]').element_by(
        have.exact_text(title)
    ).click()


@allure.step("Проверить заголовок Issue равный: {expected_title}")
def should_have_issue_title(expected_title):
    browser.element('[data-testid="issue-title"]').should(
        have.exact_text(expected_title)
    )
