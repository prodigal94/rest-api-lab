<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Api\PatientController;
use App\Http\Controllers\Api\MedicineController;
use App\Http\Controllers\Api\PrescriptionController;

Route::apiResource('patients', PatientController::class);
Route::apiResource('medicines', MedicineController::class);
Route::apiResource('prescriptions', PatientController::class);
Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');
