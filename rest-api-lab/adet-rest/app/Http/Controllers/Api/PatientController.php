<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Patient;
use Illuminate\Http\Request;

class PatientController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return response()->json(Patient::all());
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $validated = $request->validate([
            'patient_number' => 'required|unique:patients',
            'name' => 'required|string',
            'age' => 'required|integer',
            'contact_number' => 'required',
            'gender' => 'sometimes|string|nullable',
        ]);

        if (empty($validated['gender'])) {
            $validated['gender'] = 'Not specified';
        }

        $patient = Patient::create($validated);

        return response()->json([
            'message' => 'Patient registered successfully!',
            'patient' => $patient
        ], 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(Patient $patient)
    {
        return response()->json([
            'success' => true,
            'data' => $patient
        ], 200);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Patient $patient)
    {
        /*
            $table->string('name');
            $table->integer('age');
            $table->string('gender');
            $table->string('contact_number');
            $table->string('status')->default('Admitted');
        */
        $validatedData = $request->validate([
            'name' => 'sometimes|string|max:255',
            'age' => 'sometimes|integer',
            'gender' => 'sometimes|in:Male,Female',
            'contact_number' => 'sometimes|string|max:11',
            'unit_price' => 'sometimes|in:Admitted,Outpatient,Discharged',
        ]);

        $patient->update($validatedData);

        return response()->json([
            'message' => 'Patient updated successfully',
            'data' => $patient
        ], 200);
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Patient $patient)
    {
        $patient->delete();

        return response()->json([
            'success' => true,
            'message' => 'Patient deleted successfully'
        ], 200);
    }
}
