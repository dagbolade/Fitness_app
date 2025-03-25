import { ConnectButton } from '@rainbow-me/rainbowkit';
export default function WalletConnect() {
  return (
    <div className="flex justify-end mb-4">
      <ConnectButton showBalance={false} />
    </div>
  );
}