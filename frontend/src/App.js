import { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';
import HomeWallpaperImage from './assets/images/home-wallpaper.png';
import { getHints, guessCode } from "./modules/core/api";


function Modal({ isVisible, onClose, message }) {
  if (!isVisible) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div className="bg-white rounded-lg p-5 shadow-lg">
        <h2 className="text-lg font-semibold"></h2>
        <p>{message}</p>
        <button 
          onClick={onClose} 
          className="mt-4 bg-blue-500 text-white py-2 px-4 rounded">
          Close
        </button>
      </div>
    </div>
  );
}

function App() {
  const [hints, setHints] = useState([{"sequence_no": 1, text: "test"}]);
  const [code, setCode] = useState(['', '', '', '', '', '']);
  const [isModalVisible, setModalVisible] = useState(false);
  const [modalMessage, setModalMessage] = useState('');

  useEffect(() => {
    const fetchHints = async () => {
      try {
        const hintsData = await getHints();
        setHints(hintsData);
      } catch (error) {
        console.error('Error fetching hints:', error);
      }
    };

    fetchHints(); 
  }, []);

  const handleCodeChange = (index, value) => {
    const newCode = [...code];
    newCode[index] = value; // Update the specific index
    setCode(newCode); // Update state
  };

  const handleGuessCode = async () => {
    // Call the guessCode method and handle the result
    try {
      const result = await guessCode(code);
      setModalMessage(`${result.message}`); // Modify this line based on the response structure
    } catch (error) {
      setModalMessage('Error occurred while guessing the code.');
      console.error('Error guessing code:', error);
    }
    
    setModalVisible(true); // Show the modal
  };

  return (
    <div className="home">
        <img src={HomeWallpaperImage} className="home-wallpaper" alt="home-wallpaper" />
        <div class="grid place-items-center h-full">
          <div class="bg-white shadow-lg rounded-lg p-8 max-w-xs md:max-w-md w-full z-10">
              <h1 class="text-xl md:text-2xl font-bold text-center text-gray-800 mb-6">Break The Code</h1>
              <div>
                  <div class="flex space-x-2 justify-center mb-6">
                    {code.map((codeElement, index) => (
                      <input 
                        type="text" 
                        maxLength="1" 
                        class="w-10 h-10 md:w-12 md:h-12 border bg-gray-300 border-gray-300 rounded-lg text-center text-lg font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500" 
                        key={index} 
                        value={codeElement} 
                        onChange={(e) => handleCodeChange(index, e.target.value)} 
                      />
                    ))}
                  </div>
                  <button 
                    type="button" 
                    class="w-full bg-blue-500 text-white py-2 md:py-3 rounded-lg font-semibold hover:bg-blue-600 transition duration-200"
                    onClick={handleGuessCode}>
                      BREAK!
                  </button>
              </div>
          </div>
          <div>
          <h2 class="mb-2 text-lg font-semibold text-gray-900 dark:text-white">Hints</h2>
            <ul class="max-w-md space-y-1 text-gray-500 list-disc list-inside dark:text-gray-400">
                {hints.map(hint => <li key={hint.sequence_no}>{hint.text}</li>)}
            </ul>
          </div>
        </div>

        <Modal 
          isVisible={isModalVisible} 
          onClose={() => setModalVisible(false)} 
          message={modalMessage} 
        />
    </div>
  );
}

export default App;
