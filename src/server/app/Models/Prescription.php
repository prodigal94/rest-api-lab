<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use App\Models\Patient;
use App\Models\Medicine;

class Prescription extends Model
{
    protected $fillable = [
        'patient_id',
        'medicine_id',
        'doctor_name',
        'dosage',
        'quantity_dispensed',
        'prescription_date',
    ];

    public function patient()
    {
        return $this->belongsTo(Patient::class);
    }

    public function medicine()
    {
        return $this->belongsTo(Medicine::class);
    }
}
