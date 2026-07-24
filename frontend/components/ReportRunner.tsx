"use client";

import { useState } from "react";

interface ReportRunnerProps {
  onJobCreated: () => void;
}

export default function ReportRunner({
  onJobCreated
}: ReportRunnerProps){
  
  const [loading, setLoading] = useState(false);
  const [job, setJob] = useState(null);

  const generateReport = async () => {
    try {
      setLoading(true);

      const response = await fetch("http://localhost:8000/jobs", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({}),
      });

      if (!response.ok) {
        throw new Error("Failed to create report");
      }

      const data = await response.json();
      setJob(data);
      onJobCreated();
    } catch (error) {
      console.error(error);
      alert("Unable to create report.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={generateReport} disabled={loading}>
        {loading ? "Generating..." : "Generate Report"}
      </button>

      {job && (
        <div style={{ marginTop: "20px" }}>
          <h3>Job Created</h3>
           <p>ID: {job.job_id}</p>
          <p>Status: {job.status}</p>

        </div>
      )}
    </div>
  );
}
