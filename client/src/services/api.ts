import axios from 'axios';

const api = axios.create({ baseURL: process.env.REACT_APP_API_URL });
api.interceptors.response.use(res => res, err => Promise.reject(err.response?.data?.detail || err.message));
export const analyzeVideo = (url: string) => api.post('/api/v1/analyze', { url }).then(r => r.data);