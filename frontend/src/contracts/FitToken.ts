import { Contract, Signer, providers } from "ethers";
import FitTokenABI from "./FitTokenABI.json";

const CONTRACT_ADDRESS = "0xd9145CCE52D386f254917e481eB44e9943F39138"; // replace with yours

export const getFitTokenContract = (
  signerOrProvider: Signer | providers.Provider
) => {
  return new Contract(CONTRACT_ADDRESS, FitTokenABI, signerOrProvider);
};
