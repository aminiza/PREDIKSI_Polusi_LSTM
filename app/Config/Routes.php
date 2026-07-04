<?php

use CodeIgniter\Router\RouteCollection;

/** @var RouteCollection $routes */
$routes->get('/', 'Dashboard::index');

$routes->get('/forecast', 'Forecast::index');

$routes->get('/classification', 'Classification::index');

$routes->get('/documentation', 'Documentation::index');

$routes->get('/about', 'About::index');

$routes->post('/forecast/predict', 'Forecast::predict');