import WorkoutPlanCard from '../components/WorkoutPlanCard';
import TokenStats from '../components/TokenStats';
import { ConnectButton } from '@rainbow-me/rainbowkit';


export default function Home() {
  return (
    <div className="space-y-6">
      <ConnectButton />
      <h1 className="text-4xl font-bold">FitGenie Pro</h1>
      <p className="text-gray-300">Your AI-powered fitness coach with Web3 rewards.</p>
      <WorkoutPlanCard />
      <TokenStats />
    </div>
  );
}
