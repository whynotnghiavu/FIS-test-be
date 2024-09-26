import Posts from './Posts.js';


function App() {
  return (
   <>

{/* Thanh điều hướng */}
<nav className="navbar navbar-expand-md bg-dark navbar-dark">
<a className="navbar-brand" href="/"><span>📖</span></a> 
<button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
<span className="navbar-toggler-icon"></span>
</button>
<div className="collapse navbar-collapse" id="collapsibleNavbar">

<ul className="navbar-nav ml-auto">

<li className="nav-item">
<a className="nav-link" href="/">Register</a>
</li>
<li className="nav-item">
<a className="nav-link" href="/">Login</a>
</li> 
</ul>
</div>  
</nav>



<div className="col-sm-4">
<h3>Posts</h3>
<Posts  />
</div>
 



   </>
  );
}

export default App;