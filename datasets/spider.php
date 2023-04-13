<?php

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
    $data = json_decode($response);
    return $data->dataUri;
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

# just for convienence
$number_of_data = array(200, 400, 600, 800, 1000, 2000, 3000, 4000);

for ($i=0; $i < 8; $i++) { 
    //print "{$number_of_data[$i]} \n";
    for ($ii=0; $ii < $number_of_data[$i]; $ii++){
        base64_to_jpeg(fetch(), "ntust_raw_{$number_of_data[$i]}/{$ii}.png");
    }
}
