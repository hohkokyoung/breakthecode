const API_URL = 'http://localhost:8000/api/v2';

// Function to handle login
export const getHints = async () => {
  try {
    const response = await fetch(`${API_URL}/challenges/hints`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error('getHints failed');
    }

    const data = await response.json();
    const reformattedData = data.map(e => ({"sequence_no": e.sequence_no, "text": e.hint}));
    return reformattedData;
  } catch (error) {
    console.error('Error during getHints:', error);
    throw error; // Handle error appropriately
  }
};

export const guessCode = async (code) => {
    try {
        const response = await fetch(`${API_URL}/challenges/guess`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({"code": code.join("")})
        });

        if (!response.ok) {
            let failedResponse = await response.json();
            return {"success": false, "message": failedResponse.code }
        }
    
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error during getHints:', error);
        throw error; // Handle error appropriately
    }
}