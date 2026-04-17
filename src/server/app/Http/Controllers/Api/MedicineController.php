<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Medicine;
use Illuminate\Http\Request;

class MedicineController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return response()->json(Medicine::all());
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $data = $request->validate([
            'name' => 'required',
            'stock_quantity' => 'required|integer',
            'unit_price' => 'required|numeric',
        ]);

        $medicine = Medicine::create($data);

        return response()->json($medicine, 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(Medicine $medicine)
    {
        return response()->json([
            'success' => true,
            'data' => $medicine
        ], 200);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Medicine $medicine)
    {
        $validatedData = $request->validate([
            'name' => 'sometimes|string|max:255',
            'stock_quantity' => 'sometimes|integer',
            'unit_price' => 'sometimes|numeric|min:0',
        ]);

        $medicine->update($validatedData);

        return response()->json([
            'message' => 'Medicine updated successfully',
            'data' => $medicine
        ], 200);
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Medicine $medicine)
    {
        $medicine->delete();

        return response()->json([
            'success' => true,
            'message' => 'Medicine deleted successfully'
        ], 200);
    }
}
