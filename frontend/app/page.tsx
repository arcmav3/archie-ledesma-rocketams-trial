"use client";

import { useState } from "react";
import ReportRunner from "@/components/ReportRunner";
import JobList from "@/components/JobList";

export default function Page() {
  const [refresh, setRefresh] = useState(0);

  const refreshJobs = () => {
    setRefresh((prev) => prev + 1);
  };

  return (
    <main style={{padding:24}}>
      <h1>RocketAMS Report Dashboard</h1>
      <ReportRunner onJobCreated={refreshJobs} />
      <JobList refresh={refresh} />
    </main>
  );
}