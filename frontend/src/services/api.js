const API_URL = 'http://localhost:8000';  // Update this if your backend URL is different

export const classifyText = async (text) => {
    try {
        const response = await fetch(`${API_URL}/classify`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (!data.classification) {
            throw new Error('No classification received from the server');
        }

        return data;
    } catch (error) {
        console.error('Error in classifyText:', error);
        throw error;
    }
};

