'use client';

import { useEffect, useState } from "react";

export default function JobList({ refresh }) {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);

  const loadJobs = async () => {
    try {
      setLoading(true);

      const response = await fetch("http://127.0.0.1:8000/jobs");

      if (!response.ok) {
        throw new Error("Failed to load jobs");
      }

      const data = await response.json();

      setJobs(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadJobs();
  }, [refresh]);

  if (loading) {
    return <p>Loading jobs...</p>;
  }

  return (
    <div>
      <h2>Jobs</h2>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>ID</th>
            <th>Status</th>
            <th>External Job ID</th>
            <th>Report URL</th>
          </tr>
        </thead>

        <tbody>
          {jobs.map((job) => (
            <tr key={job.id}>
              <td>{job.id}</td>
              <td>{job.status}</td>
              <td>{job.external_job_id}</td>
              <td>{job.report_url}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}