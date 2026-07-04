<!-- Main Sidebar Container -->

<aside class="main-sidebar sidebar-dark-primary elevation-4">

    <!-- Brand Logo -->

    <a href="<?= base_url('/') ?>" class="brand-link">

        <span class="brand-text font-weight-light">

            <strong>ML</strong> Prediction Platform

        </span>

    </a>

    <!-- Sidebar -->

    <div class="sidebar">

        <!-- Sidebar Menu -->

        <nav class="mt-3">

            <ul class="nav nav-pills nav-sidebar flex-column"
                data-widget="treeview"
                role="menu"
                data-accordion="false">

                <!-- Dashboard -->

                <li class="nav-item">

                    <a href="<?= base_url('/') ?>" class="nav-link">

                        <i class="nav-icon fas fa-home"></i>

                        <p>Dashboard</p>

                    </a>

                </li>

                <!-- Machine Learning -->

                <li class="nav-item has-treeview menu-open">

                    <a href="#" class="nav-link active">

                        <i class="nav-icon fas fa-brain"></i>

                        <p>

                            Machine Learning

                            <i class="right fas fa-angle-left"></i>

                        </p>

                    </a>

                    <ul class="nav nav-treeview">

                        <li class="nav-item">

                            <a href="<?= base_url('classification') ?>"
                               class="nav-link">

                                <i class="far fa-circle nav-icon"></i>

                                <p>US Accident Classification</p>

                            </a>

                        </li>

                        <li class="nav-item">

                            <a href="<?= base_url('forecast') ?>"
                               class="nav-link">

                                <i class="far fa-circle nav-icon"></i>

                                <p>PM2.5 Forecasting</p>

                            </a>

                        </li>

                    </ul>

                </li>

                <!-- Documentation -->

                <li class="nav-item">

                    <a href="<?= base_url('documentation') ?>"
                       class="nav-link">

                        <i class="nav-icon fas fa-book"></i>

                        <p>Documentation</p>

                    </a>

                </li>

                <!-- About -->

                <li class="nav-item">

                    <a href="<?= base_url('about') ?>"
                       class="nav-link">

                        <i class="nav-icon fas fa-info-circle"></i>

                        <p>About Project</p>

                    </a>

                </li>

            </ul>

        </nav>

    </div>

</aside>