import ReportRunner from "../components/ReportRunner";
import JobList from "../components/JobList";

export default function Home(){
  return (
    <main style={{padding:24}}>
      <h1>RocketAMS Report Dashboard</h1>
      <ReportRunner/>
      <JobList/>
    </main>
  );
}