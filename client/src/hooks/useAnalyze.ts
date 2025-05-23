import { useContext } from 'react';
import { AnalyzeContext } from '../context/AnalyzeContext';
export const useAnalyze = () => useContext(AnalyzeContext);