<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Patient extends Model
{
    protected $fillable = ['patient_number', 'name', 'age', 'gender', 'contact_number', 'status'];
}
