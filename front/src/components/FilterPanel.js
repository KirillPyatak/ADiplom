// FilterPanel.js
import React, { useState } from 'react';

const FilterPanel = ({ onFilter }) => {
  const [formData, setFormData] = useState({
    title: '',
    authors: '',
    journal: '',
      types:''
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onFilter(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="title">Название</label>
        <input
          type="text"
          className="form-control"
          id="title"
          name="title"
          value={formData.title}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="authors">Авторы</label>
        <input
          type="text"
          className="form-control"
          id="authors"
          name="authors"
          value={formData.authors}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="journal">Журнал</label>
        <input
          type="text"
          className="form-control"
          id="journal"
          name="journal"
          value={formData.journal}
          onChange={handleChange}
        />
      </div>
        <div className="form-group">
        <label htmlFor="types">тип</label>
        <input
          type="text"
          className="form-control"
          id="types"
          name="types"
          value={formData.types}
          onChange={handleChange}
        />
      </div>
      <button type="submit" className="btn btn-primary">Применить</button>
    </form>
  );
};

export default FilterPanel;
