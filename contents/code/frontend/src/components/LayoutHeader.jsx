import React from 'react';

export default function LayoutHeader() {
  return (
   
<nav className="navbar navbar-expand-md bg-dark navbar-dark">
<a className="navbar-brand" href="/"><span>📖 BlogApp</span></a> 
<button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
<span className="navbar-toggler-icon"></span>
</button>
<div className="collapse navbar-collapse" id="collapsibleNavbar">

<ul className="navbar-nav ml-auto">

<li className="nav-item">
<a className="nav-link" href="/login">Login</a>
</li>
<li className="nav-item">
<a className="nav-link" href="/register">Register</a>
</li> 
<li className="nav-item">
<a className="nav-link" href="/setting">Setting</a>
</li> 
</ul>
</div>  
</nav>

  );
}
