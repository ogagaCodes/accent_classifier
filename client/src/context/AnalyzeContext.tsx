import React, { createContext, useState, ReactNode } from 'react';
import { analyzeVideo } from '../services/api';

interface Result { accent: string; confidence: number; summary: string; }
interface Context { result: Result | null; loading: boolean; error: string | null; analyze: (url: string) => void; }
export const AnalyzeContext = createContext<Context>({} as Context);

export const AnalyzeProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [result, setResult] = useState<Result | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const analyze = async (url: string) => {
    setLoading(true); setError(null);
    try {
      const data = await analyzeVideo(url);
      setResult(data);
    } catch (e: any) {
      setError(e.toString());
    } finally { setLoading(false); }
  };

  return (
    <AnalyzeContext.Provider value={{ result, loading, error, analyze }}>
      {children}
    </AnalyzeContext.Provider>
  );
};