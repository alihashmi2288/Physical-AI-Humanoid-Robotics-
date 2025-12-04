// src/config.ts

// By default, we use the Real API now as per user request.
// Set REACT_APP_MOCK_API='true' to revert to Mock.

export const USE_MOCK_API = false; // Set to true for mock mode without backend

// Backend API URL - Update this after deploying backend to Vercel
let internalApiUrl = 'http://localhost:8000'; // Local testing

export const setApiBaseUrl = (url: string) => {
  if (url) {
    internalApiUrl = url;
    console.log(`[Config] API Base URL set to: ${internalApiUrl}`);
  }
};

export const getApiBaseUrl = () => internalApiUrl;
