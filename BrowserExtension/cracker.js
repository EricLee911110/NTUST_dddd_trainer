const captchaCrackerAPI = `http://localhost/NTUST_dddd_trainer/BrowserExtension/index.php`;
let result = null;
let captchaBase64 = "";
let hasCalled = false;
let hasFilled = false;
$("header").css("opacity", "0");
$("footer").hide();
const interval = setInterval(() => {
    $("#Logo").attr("src", "http://localhost/NTUST_dddd_trainer/BrowserExtension/logo_only.png");
    $("#Organization").attr("src", "http://localhost/NTUST_dddd_trainer/BrowserExtension/logo.png");
    $("#Logo").css("padding", "20px");
    $("#Logo").css("width", "150px");
    $("#Logo").css("height", "150px");
    $("#Logo").css("object-fit", "cover");
    $("#Logo").css("border-radius", "50%");
    $("#Logo").css("background", "white");
    $("#Organization").css("padding", "12px");
    $("header").show();
    $("header").css("opacity", "1");
    const originalText = $("label[for='account']").html();
    $("label[for='account']").html(originalText.replace("臺科大", "臺藍大"));
    $("#Banner").hide();
    const captcha = $($(".smartCaptchaImage")[0]).attr("src");
    if ((!hasCalled || (hasCalled && captchaBase64 !== captcha)) && captcha !== undefined) {
        captchaBase64 = captcha;
        hasCalled = true;
        hasFilled = false;
        call(captchaBase64);
    }
    if (hasFilled) return;
    if (result.readyState === 4) {
        hasFilled = true;
        $($("input[data-field=captcha]")[0]).val(result.responseJSON.data.result);
    }
}, 50);
function call(code) {
    result = $.ajax({
        type: "POST",
        url: captchaCrackerAPI,
        data: {
            "captcha": code
        },
    });
}