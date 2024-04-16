import React, { useState } from 'react';
import Header from './components/Header';
import FilterPanel from './components/FilterPanel';
import PublicationList from './components/PublicationList';
import './style/PublicationList.css';
import './style/Header.css';
import './style/FilterPanel.css';
import './App.css';

function App() {
  const [searchQuery, setSearchQuery] = useState('');
  const [filterData, setFilterData] = useState({

  });

  const handleSearch = (query) => {
    setSearchQuery(query);
  };

  const handleFilter = (formData) => {
    setFilterData(formData);
  };

  return (
    <div className="App">
      <Header onSearch={handleSearch} />
      <div className="header-container">
        <FilterPanel onFilter={handleFilter} />
        {/* Отправляем отдельные данные поиска и фильтрации в компонент PublicationList */}
        <PublicationList searchQuery={searchQuery} filterData={filterData} />
      </div>
    </div>
  );
}

export default App;
