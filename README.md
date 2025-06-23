# 🧪 Автоматизированные UI-тесты для Stellar Burgers

Набор автотестов для проверки функционала сайта [Stellar Burgers](https://stellarburgers.nomoreparties.site), реализованных с использованием `pytest` и `selenium`.

---

## 📁 Описание тестовых файлов

### `test_registration.py`
Тестирует процесс регистрации нового пользователя:
- `test_registration`: успешная регистрация, последующий вход и проверка перехода на главную страницу.
- `test_password_error`: проверка ошибки при попытке регистрации с паролем короче 6 символов.

### `test_login.py`
Проверяет все доступные способы авторизации:
- `test_login_log_in_to_your_account`: вход с главной страницы через кнопку «Войти в аккаунт».
- `test_login_personal_account`: вход через кнопку «Личный кабинет».
- `test_login_from_registration_form`: вход со страницы регистрации.
- `test_login_from_recovery_form`: вход со страницы восстановления пароля.

### `test_webpage_crossing.py`
Тестирует навигацию между основными разделами и поведение авторизованного пользователя:
- `test_crossing_on_personal_cabinet`: переход в личный кабинет после авторизации.
- `test_crossing_on_main_page_through_logo`: возврат на главную через клик по логотипу.
- `test_crossing_on_main_page_through_constructor`: возврат через ссылку «Конструктор».
- `test_exit_from_account`: выход из аккаунта через личный кабинет.
- `test_crossing_chapter_buns`: переход к разделу «Булки», проверка отображения конкретного ингредиента.
- `test_crossing_chapter_sauce`: переход к разделу «Соусы», проверка отображения ингредиента.
- `test_crossing_chapter_fillings`: переход к разделу «Начинки», проверка отображения ингредиента.