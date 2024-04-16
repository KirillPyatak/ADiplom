// Header.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Header({ isAuthenticated, onSearch }) {
  const [searchQuery, setSearchQuery] = useState('');

  function handleSearch(event) {
    const query = event.target.value;
    setSearchQuery(query);
    onSearch(query); // Передаем значение поискового запроса в App
  }

  return (
    <header>
      <div>
        {/* Всплывающее меню */}
        <button>Меню</button>
      </div>
      <div>
        {/* Поисковая строка */}
        <input type="text" placeholder="Поиск..." value={searchQuery} onChange={handleSearch} />
      </div>
      <div>
        {/* Иконка профиля или ссылки для авторизации/регистрации */}
        {isAuthenticated ? (
          <Link to="/profile">Профиль</Link>
        ) : (
          <>
            <Link to="/login">Войти</Link>
            <Link to="/register">Регистрация</Link>
          </>
        )}
      </div>
    </header>
  );
}

export default Header;
