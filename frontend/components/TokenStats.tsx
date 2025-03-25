import { useState } from 'react';
import { useAccount, useWalletClient } from 'wagmi';
import { ethers } from 'ethers';
import FitTokenABI from '../src/contracts/FitTokenABI.json'; // adjust path if needed

const CONTRACT_ADDRESS = '0xf8e81D47203A594245E36C48e151709F0C19fBe8'; // your deployed Remix VM address

const TokenStats = () => {
  const { address, isConnected } = useAccount();
  const { data: walletClient } = useWalletClient();
  const [status, setStatus] = useState<string | null>(null);

  const handleMint = async () => {
    if (!walletClient || !address) {
      setStatus('Wallet not connected or client unavailable');
      return;
    }

    try {
      const provider = new ethers.BrowserProvider(window.ethereum);
      const signer = await provider.getSigner();

      const contract = new ethers.Contract(CONTRACT_ADDRESS, FitTokenABI, signer);
      const tx = await contract.mint(address, ethers.parseUnits("10", 18)); // mint 10 FIT tokens
      setStatus('Transaction sent. Waiting for confirmation...');
      await tx.wait();
      setStatus('✅ 10 FIT tokens minted successfully!');
    } catch (err) {
      console.error(err);
      setStatus('❌ Minting failed');
    }
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mt-6">$FIT Token Stats</h2>
      <p>Tokens Earned: 25</p>
      <p>Workout Streak: 4 days</p>
      <br />
      {isConnected ? (
        <button
          onClick={handleMint}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Mint FIT Token
        </button>
      ) : (
        <p className="text-red-500">Connect your wallet to mint tokens.</p>
      )}
      {status && <p className="mt-2 text-sm">{status}</p>}
    </div>
  );
};

export default TokenStats;
