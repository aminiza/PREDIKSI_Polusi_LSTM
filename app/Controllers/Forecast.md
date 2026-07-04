<?php

namespace App\Controllers;

use Config\Services;

class Forecast extends BaseController
{
    public function index()
    {
        return view('forecast/index', [
            'title' => 'PM2.5 Forecasting'
        ]);
    }

    public function predict()

    {
        $file = $this->request->getFile('dataset');

        if (!$file || !$file->isValid()) {

            return redirect()->back()->with('error', 'Silakan pilih file CSV.');
        }

        if ($file->getExtension() != 'csv') {

            return redirect()->back()->with('error', 'File harus berformat CSV.');
        }

        // Membuat nama file baru agar tidak bentrok
        $newName = $file->getRandomName();

        // Simpan ke folder writable/uploads
        $file->move(WRITEPATH . 'uploads', $newName);

        $filePath = WRITEPATH.'uploads/'.$newName;

        // dd([
        //     file_exists($filePath),
        //     $filePath
        // ]);

        //--------------------------------------------------
        // Kirim File ke Flask API
        //--------------------------------------------------

        $client = Services::curlrequest();

        try {

            $response = $client->request('POST', 'http://127.0.0.1:5000/predict', [

                'multipart' => [

                    [

                        'name' => 'file',

                        'contents' => fopen(
                            WRITEPATH . 'uploads/' . $newName,
                            'r'
                        ),

                        'filename' => $newName

                    ]

                ]

            ]);

            $result = json_decode($response->getBody(), true);
            return redirect()->back()->with('prediction', $result);
        } catch (\Exception $e) {

            dd($e->getMessage());
        }
    }
}
