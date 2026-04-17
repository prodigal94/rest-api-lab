<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Prescription;
use Illuminate\Http\Request;

class PrescriptionController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return response()->json(Prescription::with(['patient', 'medicine'])->get());
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $validated = $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'medicine_id' => 'required|exists:medicines,id',
            'doctor_name' => 'sometimes|string|nullable|max:255',
            'dosage' => 'required|string|max:255',
            'quantity_dispensed' => 'required|integer|min:1',
            'prescription_date' => 'sometimes|date',
        ]);

        // Reduce the stock of medicine after prescription is validated
        $prescription = DB::transaction(function () use ($validated) {
            $medicine = Medicine::findOrFail($validated['medicine_id']);
            
            if ($medicine->stock_quantity < $validated['quantity_dispensed']) {
                throw new \Exception("Insufficient stock for {$medicine->name}");
            }
            
            $medicine->decrement('stock_quantity', $validated['quantity_dispensed']);
            
            return Prescription::create($validated);
        });

        return response()->json([
            'message' => 'Prescription created successfully',
            'data' => $prescription->load(['patient', 'medicine'])
        ], 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(Prescription $prescription)
    {
        return response()->json([
            'success' => true,
            'data' => $prescription->load(['patient', 'medicine'])
        ], 200);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Prescription $prescription)
    {
        $validatedData = $request->validate([
            'patient_id' => 'sometimes|exists:patients,id',
            'medicine_id' => 'sometimes|exists:medicines,id',
            'doctor_name' => 'sometimes|string|nullable|max:255',
            'dosage' => 'sometimes|string|max:255',
            'quantity_dispensed' => 'sometimes|integer|min:1',
            'prescription_date' => 'sometimes|date',
        ]);

        $prescription->update($validatedData);

        return response()->json([
            'message' => 'Prescription updated successfully',
            'data' => $prescription->load(['patient', 'medicine'])
        ], 200);
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Prescription $prescription)
    {
        $prescription->delete();

        return response()->json([
            'success' => true,
            'message' => 'Prescription deleted successfully'
        ], 200);
    }
}
