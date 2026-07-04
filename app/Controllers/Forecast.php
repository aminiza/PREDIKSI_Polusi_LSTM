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

        //--------------------------------------------------
        // Kirim File ke Flask API
        //--------------------------------------------------
        $client = Services::curlrequest();

        // 1. Pastikan path file didefinisikan dengan benar
        $filePath = WRITEPATH . 'uploads/' . $newName;

        try {
            $response = $client->request('POST', 'http://127.0.0.1:5000/predict', [
                'http_errors' => false,
                
                // 2. Gunakan struktur array CI4 native dengan \CURLFile
                'multipart' => [
                    'file' => new \CURLFile($filePath, 'text/csv', $newName)
                ]
            ]);

            $result = json_decode($response->getBody(), true);
            
            if (isset($result['status']) && $result['status'] === 'error') {
                return redirect()->back()->with('error', 'Prediksi gagal: ' . $result['message']);
            }

            return redirect()->back()->with('prediction', $result);

        } catch (\Exception $e) {
            return redirect()->back()->with('error', 'Koneksi ke API Gagal: ' . $e->getMessage());
        }
    }
}
