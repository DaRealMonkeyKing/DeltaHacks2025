// Create a config file for your API URL
export const API_URL = process.env.NODE_ENV === 'production' 
  ? 'https://your-backend-domain.com'
  : 'http://localhost:5000'; 