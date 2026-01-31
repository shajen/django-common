$(document).ready(updateFieldsFilter);

function updateFieldsFilter() {
    $.datetimepicker.setLocale('pl');
    params = new URLSearchParams(window.location.search);
    for (p of params) {
        field = $("#input_" + p[0]);
        field.val(p[1]);
        field.prop("checked", true);
    }
    $("input[id^=input_]").each(function () {
        const inputType = $(this).attr('input-type');
        if (inputType == "datetime") {
            $(this).datetimepicker({ format: 'Y-m-d H:i', dayOfWeekStart: 1 });
        }
        else if (inputType == "date") {
            $(this).datetimepicker({ format: 'Y-m-d', dayOfWeekStart: 1, timepicker: false });
        }
        else if (inputType == "duration") {
            $(this).timepicker({
                showSeconds: true,
                showMeridian: false,
                secondStep: 1,
                minuteStep: 1,
                defaultTime: false,
                icons: { up: 'bi bi-chevron-compact-up', down: 'bi bi-chevron-compact-down' }
            });
        }
    });
    $("input[id^=input_][id*='_option_']").change(function () {
        const id = $(this).attr('field-id');
        const value = $(this).val();
        $("#" + id).val(value);
    });
}
