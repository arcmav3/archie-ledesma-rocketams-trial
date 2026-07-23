'use client';

export default function ReportRunner(){
  return (
    <div>
      <h2>Run Report</h2>
      <select>
        <option>SALES_AND_TRAFFIC</option>
        <option>FBA_INVENTORY</option>
        <option>SETTLEMENT</option>
      </select>
      <button>Run</button>
    </div>
  );
}