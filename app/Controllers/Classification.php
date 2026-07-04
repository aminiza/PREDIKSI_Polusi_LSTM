<?php

namespace App\Controllers;

class Classification extends BaseController
{
    public function index()
    {
        return view('classification/index', [
            'title' => 'US Accident Classification'
        ]);
    }
}