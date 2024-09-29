import React, { useEffect, useState } from 'react';

const Categories = () => {
  const [categories, setCategories] = useState([]);

  // Fetch categories when the component mounts
  useEffect(() => {
    fetch('https://127.0.0.1:8080/api/v1/categories?skip=0&limit=100', {
      headers: {
        'accept': 'application/json',
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        setCategories(data); // Save the data to state
      })
      .catch((error) => {
        console.error('Error fetching categories:', error);
      });
  }, []);

  return (
    <div className="container">
      <div className="row">
        <div className="col-sm-4">
          <ul className="nav nav-pills flex-column">
            {categories.map((category) => (
              <li className="nav-item" key={category.id}>
                <a className="nav-link" href="/">
                  {category.name}
                </a>
              </li>
            ))}
          </ul>
          {/* <hr className="d-sm-none" /> */}
        </div>
      </div>
    </div>
  );
};

export default Categories;
