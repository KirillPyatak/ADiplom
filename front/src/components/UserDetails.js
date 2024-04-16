// components/UserDetails.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function UserDetails() {
  const { id } = useParams();
  const [user, setUser] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/api/accounts/User/${id}/`)
      .then(response => {
        setUser(response.data);
      })
      .catch(error => {
        console.error('Error fetching user details:', error);
      });
  }, [id]);

  return (
    <div>
      {user ? (
        <div>
          <h2>User Details</h2>
          <p>Name: {user.name}</p>
          <p>Email: {user.email}</p>
          <p>Scientific Activity:</p>
          <ul>
            <li>Publication Count: {user.scientific_activity.publication_count}</li>
            <li>Citation Count: {user.scientific_activity.citation_count}</li>
            <li>Impact Factor: {user.scientific_activity.impact_factor}</li>
          </ul>
        </div>
      ) : (
        <p>Loading user details...</p>
      )}
    </div>
  );
}

export default UserDetails;
