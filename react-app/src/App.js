import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Spotify Playlist Generator</h1>
        <p>The current time is {currentTime}.</p>
      </header>
      <form>
        <label>
          Playlist Name:
          <input type="text" name="name" />
        </label><br/>
        <label>
          Playlist Description:
          <input type="text" name="desc" />
        </label><br/>
        <label>
          API Key
          <input type="text" name="apikey" />
        </label><br/>
        <label>Artist Song Separator   </label>
        <select>
          <option value="comma">,</option>
          <option selected value="dash">-</option>
          <option value="slash">/</option>
        </select><br/>
        <label>
          Playlist<br/>
          <textarea/>
        </label><br/>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

export default App;
