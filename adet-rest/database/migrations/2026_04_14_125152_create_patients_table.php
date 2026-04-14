<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('patients', function (Blueprint $table) {
            $table->id();
            $table->string('patient_number')->unique();
            $table->string('name');
            $table->integer('age');
            $table->string('gender');
            $table->string('blood_type')->nullable();
            $table->string('contact_number');
            $table->text('address')->nullable();
            $table->dateTime('admission_date')->useCurrent();
            $table->string('status')->default('Admitted');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('patients');
    }
};
