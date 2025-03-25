import './index.css';
import '@rainbow-me/rainbowkit/styles.css';

import {
  getDefaultConfig,
  RainbowKitProvider,
} from '@rainbow-me/rainbowkit';

import { WagmiProvider, http } from 'wagmi';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

import { mainnet } from 'wagmi/chains';
import { ReactNode } from 'react';
import Home from '../pages/Home';


const config = getDefaultConfig({
  appName: 'FitGenie Pro',
  projectId: '4b3d6565d77868330be024eb9d60fb1e', // Replace with WalletConnect ID or temp key
  chains: [mainnet],
  transports: {
    [mainnet.id]: http()
  }
});

const queryClient = new QueryClient();
console.log("FitGenie is LIVE 🚀");

export default function App(): ReactNode {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <RainbowKitProvider>
          <Home />
        </RainbowKitProvider>
      </QueryClientProvider>
    </WagmiProvider>
  );
}
