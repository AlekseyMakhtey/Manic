document.addEventListener('DOMContentLoaded', function () {
    // Валидация формы (клиентская, не мешающая серверным ошибкам)
    (function () {
        'use strict'
        var forms = document.querySelectorAll('.needs-validation')
        Array.prototype.slice.call(forms)
            .forEach(function (form) {
                form.addEventListener('submit', function (event) {
                    // Проверяем только клиентскую валидацию, если серверные ошибки еще не обработаны
                    if (!form.checkValidity() && !form.querySelector('.error-message')) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
    })()

    // Анимация появления формы
    const formWrapper = document.querySelector('.form-wrapper')
    formWrapper.classList.add('animate__animated', 'animate__fadeInUp')

    // Пульсация кнопки
    const submitBtn = document.querySelector('.submit-btn')
    submitBtn.addEventListener('mouseover', function () {
        this.classList.add('animate__pulse')
    })
    submitBtn.addEventListener('mouseout', function () {
        this.classList.remove('animate__pulse')
    })

    // Закрытие сообщения об ошибке
    const closeBtn = document.querySelector('.close-btn')
    if (closeBtn) {
        closeBtn.addEventListener('click', function () {
            this.parentElement.style.display = 'none'
        })
    }
})