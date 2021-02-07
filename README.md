
<!DOCTYPE html>
<!--[if (gt IE 9)|!(IE)]><!--> <html class="no-js" lang="pt-br"> <!--<![endif]-->
  <head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Language" content="pt-br">
    <!-- www.phpied.com/conditional-comments-block-downloads/ -->
    <!-- Always force latest IE rendering engine
         (even in intranet) & Chrome Frame
         Remove this if you use the .htaccess -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <!--  Mobile Viewport Fix
          j.mp/mobileviewport & davidbcalhoun.com/2010/viewport-metatag
          device-width: Occupy full width of the screen in its current orientation
          initial-scale = 1.0 retains dimensions instead of zooming out if page height > device height
          user-scalable = yes allows the user to zoom in -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>model_two</title>
    <!-- http://dev.w3.org/html5/markup/meta.name.html -->
    <meta name="application-name" content="model_two">
    <!-- Speaking of Google, don't forget to set your site up:
         http://google.com/webmasters -->
    <meta name="google-site-verification" content="">
    <!-- include stylesheets -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="/model_two/static/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="/model_two/static/css/web2py-bootstrap4.css"/>
    <link rel="shortcut icon" href="/model_two/static/images/ico.ico" type="image/x-icon">
    <link rel="apple-touch-icon" href="/model_two/static/images/icone.png">
      <!-- importando temas para testar -->
    <link rel="stylesheet" href="https://bootswatch.com/4/spacelab/bootstrap.css"/>
    <!-- All JavaScript at the bottom, except for Modernizr which enables
         HTML5 elements & feature detects -->
    <script src="/model_two/static/js/modernizr-2.8.3.min.js"></script>
    <!-- Favicons -->
    <script type="text/javascript"><!--
    // These variables are used by the web2py_ajax_init function in web2py_ajax.js (which is loaded below).
    var w2p_ajax_datetime_format = "%d-%m-%Y %H:%M:%S";
var w2p_ajax_date_format = "%d-%m-%Y";
var w2p_ajax_confirm_message = "Voc\u00ea tem certeza que quer apagar este objeto?";
var ajax_error_500 = "Ocorreu um erro, por favor <a href=\"/model_two/default/index\">reload</a> a p\u00e1gina";
var w2p_ajax_disable_with_message = "Trabalhando...";

    //--></script>

<meta name="keywords" content="[&#x27;web2py&#x27;, &#x27;python&#x27;, &#x27;framework&#x27;]" />
<meta name="description" content="a cool new app" />
<meta name="generator" content="Web2py Web Framework" />
<meta name="author" content="Your Name &lt;you@example.com&gt;" />
<script src="/model_two/static/js/jquery.js" type="text/javascript"></script><link href="/model_two/static/css/calendar.css" rel="stylesheet" type="text/css" /><script src="/model_two/static/js/calendar.js" type="text/javascript"></script><script src="/model_two/static/js/web2py.js" type="text/javascript"></script>
 <!-- this includes jquery.js, calendar.js/.css and web2py.js -->
    
  </head>
  <body>
      <style  type="text/css">
    @media print{
        .btn{
             display: none;
        }
        
        #noprint { display:none; } 
      a:link{font:15px "verdana"; color:#8B4513; text-decoration:none;}

a:hover{font:20px "verdana"; color:black; text-decoration:underline;}
    }
      </style>
    <div class="w2p_flash alert alert-dismissable"></div>
    <!-- Navbar ======================================= -->
    <nav class="navbar navbar-light navbar-expand-md bg-faded bg-dark navbar-dark justify-content-center">
       <a href="#" class="navbar-brand d-flex w-50 mr-auto">Sistema</a>
       <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="navbar-collapse collapse w-100" id="navbarNavDropdown">
         <ul class="navbar-nav w-100 justify-content-center">
          
          
          <li class="nav-item ">
            <a class="nav-link" href="/model_two/acs_sistema/index">Principal</a>
          </li>
          
          
          
          <li class="nav-item ">
            <a class="nav-link" href="/model_two/acs_clientes/index">Clientes</a>
          </li>
          
          
          
          <li class="nav-item ">
            <a class="nav-link" href="/model_two/acs_imoveis/index">Imóveis</a>
          </li>
          
          
          
          <li class="nav-item ">
            <a class="nav-link" href="/model_two/acs_recebimentos/index">Recebimentos</a>
          </li>
          
          
        </ul>
       
        
        <ul class="nav navbar-nav ml-auto w-100 justify-content-end">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Rogoberto
            </a>
            <div class="dropdown-menu dropdown-menu-right">
              
              <a class="dropdown-item" href="/model_two/default/user/profile">Profile</a>
              
              <a class="dropdown-item" href="/model_two/default/user/change_password">Change Password</a>
              
              <a class="dropdown-item" href="/model_two/default/user/logout">Logout</a>
              
            </div>
          </li>
        </ul>
        
      </div>
    </nav>

    <!-- Masthead ===================================== -->
    
    
    <!-- Main ========================================= -->
    <!-- Begin page content -->
    <div class="container-fluid main-container pb-5">
        <div class=" pb-5">
            
      

  <head>
<meta name="application-name" content="Rogoberto">
</head>
<style>
    .animate-in-left {
        transition: all 1.0s ease-out;
        position:relative;
        opacity:1;
        left:0%;
        &.out-of-viewport {
            opacity:0;left:-5%;
        }
    }

    .animate-in-right {
        transition: all 1.0s ease-out;
        position:relative;
        opacity:1;
        left:0%;
        &.out-of-viewport {
            opacity:0;
            left:5%;
        }
    }
</style>
<div class="py-5" >
    <div class="container">
      <div class="row">
        <div class="px-5 col-md-8 text-center mx-auto">
          <h3 class="text-primary display-4"> <b>Arsenal System</b> </h3>
          <h2 class="my-3">Alugueis e Recebimentos.</h2>
          <p class="mb-3">Compreender e manter o padrão em processos deve ser o objetivo principal de qualquer negocio, faça isso de maneira simples.</p> 
            <a href="https://arsenalsystem.pythonanywhere.com/model_two/acs_sistema/index" class="btn btn-primary">Acessar</a>
        </div>
      </div>
    </div>
  </div>

  <div class="py-5">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="row">
            <div class="col-md-4 col-lg-3 order-1 order-md-2 p-0"> 
              <img class="img-fluid d-block  animate-in-left" src="/model_two/default/download/artigo.imagem.915230f67e2dd131.666f746f2d3632302d3435352e6a7067.jpg" />
              </div>
            <div class="d-flex flex-column justify-content-center p-3 col-md-8 offset-lg-1 align-items-start order-2 order-md-2">
              <h3>Um Sistema para Gerar Contratos</h3>
              <p class="mb-3">Manter um processo padrão entre todos os contratos gerados, nosso setor jurídico tem o melhor contrato de locação para o seu negocio, mantenha o padrão em todos os seus contratos e alem do mais faça isso automaticamente..</p> <a class="btn btn-primary" href="https://api.whatsapp.com/send?phone=5588981126816">Entre em Contato</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="py-5">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="row">
            <div class="d-flex flex-column justify-content-center p-3 col-md-8 offset-lg-1 align-items-start order-2 order-md-1">
              <h3>Controle Tudo Através Celular</h3>
              <p class="mb-3">Não importa aonde esteja, se estiver com o celular na mão estará com seu negocio à vista, não existe nada melhor que o supervisionamento do responsável pelos recebimentos dos rendimentos financeiros.</p> <a class="btn btn-primary" href="https://api.whatsapp.com/send?phone=5588981126816">Entre em Contato</a>
            </div>
            <div class="col-md-4 col-lg-3 order-1 order-md-2 p-0"> 
              <img class="img-fluid d-block animate-in-right" src="/model_two/default/download/artigo.imagem.95da570d173dd96a.6f6e6c696e652d323930303330335f3936305f3732302e6a7067.jpg" /></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="py-3 text-center">
    <div class="container">
      <div class="row">
        <div class="col-md-12 text-center">
          <h1>Características</h1>
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-md-4 p-4"> <i class="d-block fa fa-circle fa-3x mb-2 text-muted "></i>
          <h4> <b>Departamentalização</b> </h4>
          <p>A departamentalização das funções dentro da sua organização precisam ser bem definidas e com restrições entre acessos, o usuário administrativo tem acesso a custos e investimentos relatórios para facilitar a tomada de decisões.</p>
        </div>
        <div class="col-md-4  p-4"> <i class="d-block fa fa-stop-circle-o fa-3x mb-2 text-muted"></i>
          <h4> <b>Multiplataforma</b> </h4>
          <p>Nosso sistema funciona de maneira descentralizada, com um banco de dados em nuvem o acesso aos dados se dá por meio do navegador podendo ser acessado independentemente da plataforma que esteja utilizando, seja um computador, notebook, android, iphone qualquer outra plataforma.
.</p>
        </div>
        <div class="col-md-4  p-4"> <i class="d-block fa fa-circle-o fa-3x mb-2 text-muted"></i>
          <h4> <b>Tecnologia PWA</b> </h4>
          <p>A maior vantagem de um PWA em comparação a um aplicativo é que o problema do cliente pode ser solucionado imediatamente necessidade de que ele baixe um aplicativo. Um cliente utiliza o PWA não terá a necessidade de desinstalá-lo uma vez que esse não traz sobrecarga ao aparelho usado..</p>
        </div>
      </div>
    </div>
  </div>
  <div class="py-5 text-center">
    <div class="container">
      <div class="row">
        <div class="mx-auto col-md-12">
          <h1 class="mb-3">Equipe</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-3  p-4"> <img class="img-fluid d-block mb-3 mx-auto rounded-circle" src="/model_two/default/download/desenvolvedor.imagem.b3f2fa9e0e93eaa5.4c756d69695f32303230303732355f3039323635313133342e6a7067.jpg" width="100" alt="Card image cap">
          <h4> <b>Rogoberto Ribeiro</b> </h4>
          <p>CEO e Fundador</p>
          <p class="mb-0"> <i>"São as coisas simples as melhores, sofisticação é simplicar de forma inteligentes"</i> </p>
        </div>
        <div class="col-lg-3 p-4"> <img class="img-fluid d-block mb-3 mx-auto rounded-circle" src="/model_two/default/download/desenvolvedor.imagem.ba148b100e93b32b.30303030322e706e67.png" width="100" alt="Card image cap">
          <h4> <b>Betinho</b> </h4>
          <p>Desenbolvedor</p>
          <p class="mb-0"> <i>"O impossivel é só questão de opinião"</i> </p>
        </div>
        <div class="col-lg-3 p-4"> <img class="img-fluid d-block mb-3 mx-auto rounded-circle" src="/model_two/default/download/desenvolvedor.imagem.841ae2403c9159de.30303030312e706e67.png" width="100">
          <h4> <b>Helena Oliveira</b> </h4>
          <p>Designer</p>
          <p class="mb-0"> <i>"Funcional e bonito são premissas de qualquer atividade"</i> </p>
        </div>
        <div class="col-lg-3  p-4"> <img class="img-fluid d-block mb-3 mx-auto rounded-circle" src="/model_two/default/download/desenvolvedor.imagem.b9dbf7155dd5d436.303030332e6a7067.jpg" width="100">
          <h4> <b>quarto</b> </h4>
          <p>CEO e Fundador</p>
          <p class="mb-0"> <i>"O impossivel é só questão de opinião"</i> </p>
        </div>
      </div>
    </div>
  </div>

      
    </div>
        </div>

     <!-- this is default footer -->
<footer class="footer container-fluid bg-faded bg-dark">
      <div class="row">
        <div class="col-md-12">
          <div class="copyright pull-left">
              <h6 class="text-white" >
              Copyright &#169; 2021
              </h6>
            </div>
          <div id="poweredBy" class="pull-right">
              <h6 class="text-white">
            Suporte
            <a href="#">(88)8112-6816</a>
              </h6>
          </div>
      <div class="row">
        </div>
        </div>
      </div>
    </footer>
    
    <!-- The javascript =============================== -->
    <script src="/model_two/static/js/bootstrap.bundle.min.js"></script>
    <script src="/model_two/static/js/web2py-bootstrap4.js"></script>
    
    
  </body>
</html>
