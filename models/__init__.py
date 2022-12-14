from .base import *
from .vanilla_vae import *
from .gamma_vae import *
from .beta_vae import *
from .wae_mmd import *
from .cvae import *
from .hvae import *
from .vampvae import *
from .iwae import *
from .dfcvae import *
from .mssim_vae import MSSIMVAE
from .fvae import *
from .cat_vae import *
from .joint_vae import *
from .info_vae import *

# Aliases
VAE = VanillaVAE
GaussianVAE = VanillaVAE
CVAE = ConditionalVAE
GumbelVAE = CategoricalVAE

vae_models = {'VanillaVAE':VanillaVAE,
              'WAE_MMD':WAE_MMD,
              'ConditionalVAE':ConditionalVAE,
              'BetaVAE':BetaVAE,
              'GammaVAE':GammaVAE,
              'HVAE':HVAE,
              'VampVAE':VampVAE,
              'IWAE':IWAE,
              'DFCVAE':DFCVAE,
              'MSSIMVAE':MSSIMVAE,
              'FactorVAE':FactorVAE,
              'CategoricalVAE':CategoricalVAE,
              'JointVAE':JointVAE,
              'InfoVAE':InfoVAE}
