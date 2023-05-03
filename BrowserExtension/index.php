<?php
$python_path = "/usr/local/bin/python3.9";
$cracker_file = "./cracker.py";
if (!isset($_POST['captcha'])) die();
//header("Access-Control-Allow-Origin: *");
//header("Access-Control-Allow-Methods: *");
//header("Access-Control-Allow-Headers: Origin, Methods, Content-Type");

$result = cracker();
//while (!is_numeric($result["result"]) || !verify($result["hash"], $result["result"])) {
//    $result = cracker();
//}
ok($result);

function cracker() {
    global $python_path;
    global $cracker_file;
    $cmd = $python_path . " " . realpath($cracker_file);
//    $data = fetch();
//    $hash = $data->captcha;
    base64_to_jpeg($_POST['captcha'], "captcha.png");
    $result = shell_exec($cmd);
    return [
        "hash" => "",
        "image" => "",
        "result" => str_replace("\n", "", $result),
    ];
}

function base64_to_jpeg($base64_string, $output_file) {
    // open the output file for writing
    $ifp = fopen( $output_file, 'wb' );

    // split the string on commas
    // $data[ 0 ] == "data:image/png;base64"
    // $data[ 1 ] == <actual base64 string>
    $data = explode( ',', $base64_string );

    // we could add validation here with ensuring count( $data ) > 1
    fwrite( $ifp, base64_decode( $data[ 1 ] ) );

    // clean up the file resource
    fclose( $ifp );

    return $output_file;
}

function ok($data) {
    header("Content-Type: application/json");
    echo json_encode([
        "success" => true,
        "data" => $data
    ]);
//    header("Connection: close");
}

function verify($hash, $ans) {
    $data = '{"username":"","password":"","captcha":"{\"captcha\":\"KXuPL01-11BXEn5Vndn_8aIAq8UUbg0gbyK9ap96kE9Wq8cRiW1UdDvdlFJhf62vzXNStqUJsxz9pbEeOCrEjw\",\"val\":\"123123123\"}","HiddenOTP":"false","SourceUriLocation":"https://mail.ntust.edu.tw/","LoginSystem_Image":"","LoginSystem_Url":"","BackGroundColor":"","LoginState":false,"LoginPage":"","LogoutPage":"","type":"","host":"","ip":null,"mac":null,"essid":null,"apname":null,"apgroup":null,"returnUrl":"","isMobile":false,"wirelessSystem":"","loginBtnHtml":"登入（Login）","kendoParam":{"kendoCmd":"","kendoAction":"modify"},"currentPage":0}';
    $data = json_decode($data, true);

    $data_captcha = json_decode($data["captcha"]);
    $data_captcha->captcha = $hash;
    $data_captcha->val = $ans;

    // update
    $data["captcha"] = json_encode($data_captcha);

    $curl = curl_init();

    curl_setopt_array($curl, array(
        CURLOPT_URL => 'https://login.ntust.edu.tw/Login/createLogin',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS => json_encode($data),
        CURLOPT_HTTPHEADER => array(
            'Content-Type: application/json',
            'Cookie: UqZBpD3n3iPIDwJU9A2tuWuNAPYa849FPYGU=v1HM1YBQSDft1'
        ),
    ));

    $response = curl_exec($curl);

    curl_close($curl);
    return str_contains($response, "System.NullReferenceException");
}

function fetch() {
    $curl = curl_init();

    curl_setopt_array($curl, array(
        CURLOPT_URL => 'https://login.ntust.edu.tw/generalAPI/getCaptcha',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'GET',
        CURLOPT_HTTPHEADER => array(
            'Cookie: UqZBpD3n3iPIDwJU9A2tuWuNAPYa849FPYGU=v1HM1YBQSDft1'
        ),
    ));

    $response = curl_exec($curl);

    curl_close($curl);
    return json_decode($response);
}