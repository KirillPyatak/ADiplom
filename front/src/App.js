// App.js
import React, { useState } from 'react';
import FilterPanel from './components/FilterPanel';
import PublicationList from './components/PublicationList';
import Header from './components/Header';
import './style/PublicationList.css';
import './style/Header.css';
import './style/FilterPanel.css';
import './App.css';

function App() {
  const [filterParams, setFilterParams] = useState({
    title: '',
    authors: '',
    journal: '',
    types: ''
  });
  const isAuthenticated = true; // or false, depending on your authentication logic

  const handleFilter = (formData) => {
    setFilterParams(formData);
  };

  return (
    <div className="App">
      <Header isAuthenticated={isAuthenticated} />
      <div className="header-container">
        <FilterPanel onFilter={handleFilter} />
        <PublicationList filterParams={filterParams} />
      </div>
    </div>
  );
}

export default App;
